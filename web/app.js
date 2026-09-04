/* global initSqlJs */
const loading = document.querySelector('#loading');
const app = document.querySelector('#app');
const search = document.querySelector('#search');
const results = document.querySelector('#results');
const resultCount = document.querySelector('#result-count');
const detail = document.querySelector('#exercise-detail');
const summary = document.querySelector('#summary');
const tableSelect = document.querySelector('#table-select');
const tableCount = document.querySelector('#table-count');
const tableView = document.querySelector('#table-view');
let database;
let selectedExercise;

const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#039;' })[char]);
const query = (sql, params = []) => {
  const statement = database.prepare(sql);
  statement.bind(params);
  const rows = [];
  while (statement.step()) rows.push(statement.getAsObject());
  statement.free();
  return rows;
};
const scalar = (sql, params = []) => query(sql, params)[0]?.value;
const display = value => value === null || value === undefined || value === '' ? '—' : escapeHtml(value);

function renderSummary() {
  const exercises = scalar('SELECT COUNT(*) AS value FROM exercises');
  const translations = scalar('SELECT COUNT(*) AS value FROM exercise_translations');
  const languages = scalar('SELECT COUNT(*) AS value FROM languages');
  const version = scalar("SELECT value FROM metadata WHERE key = 'version'") || 'local build';
  summary.innerHTML = `<span class="stat"><strong>${exercises}</strong> exercises</span><span class="stat"><strong>${translations}</strong> translations</span><span class="stat"><strong>${languages}</strong> languages</span><span class="stat">version <strong>${escapeHtml(version)}</strong></span>`;
}

function findExercises() {
  const term = search.value.trim();
  const like = `%${term}%`;
  const rows = query(`SELECT DISTINCT e.id, e.slug, e.status,
    COALESCE(MAX(CASE WHEN t.language_code = 'en' THEN t.name END), MIN(t.name), e.slug) AS title
    FROM exercises e LEFT JOIN exercise_translations t ON t.exercise_id = e.id
    WHERE ? = '' OR e.id = ? OR lower(t.name) LIKE lower(?)
    GROUP BY e.id ORDER BY title COLLATE NOCASE LIMIT 150`, [term, term, like]);
  resultCount.textContent = `${rows.length}${rows.length === 150 ? '+' : ''} result${rows.length === 1 ? '' : 's'}${term ? ` for “${term}”` : ''}`;
  results.innerHTML = rows.length ? rows.map(row => `<button class="result ${row.id === selectedExercise ? 'selected' : ''}" data-id="${escapeHtml(row.id)}">${escapeHtml(row.title)}<small>#${escapeHtml(row.id)} · ${escapeHtml(row.status)} · ${escapeHtml(row.slug)}</small></button>`).join('') : '<div class="result">No matching exercise.</div>';
  results.querySelectorAll('button').forEach(button => button.addEventListener('click', () => showExercise(button.dataset.id)));
}

function listValues(sql, id, formatter) { return query(sql, [id]).map(formatter).join('') || '<span class="tag">None</span>'; }
function showExercise(id) {
  selectedExercise = id;
  const exercise = query('SELECT * FROM exercises WHERE id = ?', [id])[0];
  const translations = query('SELECT * FROM exercise_translations WHERE exercise_id = ? ORDER BY language_code', [id]);
  const muscles = listValues(`SELECT em.role, COALESCE(mt.name, em.muscle_id) AS name FROM exercise_muscles em
    LEFT JOIN muscle_translations mt ON mt.muscle_id = em.muscle_id AND mt.language_code = 'en' WHERE em.exercise_id = ? ORDER BY em.role, name`, id, row => `<span class="tag">${escapeHtml(row.name)} · ${escapeHtml(row.role)}</span>`);
  const equipment = listValues('SELECT equipment_id, kind FROM exercise_equipment WHERE exercise_id = ? ORDER BY kind, equipment_id', id, row => `<span class="tag">${escapeHtml(row.equipment_id)} · ${escapeHtml(row.kind)}</span>`);
  const tags = listValues('SELECT tag FROM exercise_tags WHERE exercise_id = ? ORDER BY tag', id, row => `<span class="tag">${escapeHtml(row.tag)}</span>`);
  const factKeys = ['id','slug','status','merged_into','modality','mechanic','force_vector','movement_pattern','laterality','difficulty','tracking_type','load_mode','supports_added_weight','primary_equipment','body_region','category_name','muscles_primary','muscles_secondary','image_path','is_custom','created_by','source','upstream_source','upstream_id','upstream_license','upstream_license_author'];
  detail.classList.remove('empty');
  detail.innerHTML = `<h2>${escapeHtml(translations.find(t => t.language_code === 'en')?.name || exercise.slug)}</h2><p class="meta">Exercise #${escapeHtml(id)} · complete database record</p><h3>Exercise record</h3><div class="data-grid">${factKeys.map(key => `<div class="field"><small>${escapeHtml(key)}</small>${display(exercise[key])}</div>`).join('')}</div><h3>Muscles</h3><div class="relation-list">${muscles}</div><h3>Equipment</h3><div class="relation-list">${equipment}</div><h3>Usage tags</h3><div class="relation-list">${tags}</div><h3>Translations (${translations.length})</h3>${translations.map(t => `<section class="translation"><strong>${escapeHtml(t.language_code)} · ${escapeHtml(t.name)}</strong><div class="data-grid"><div class="field"><small>status</small>${display(t.status)}</div><div class="field"><small>source_lang</small>${display(t.source_lang)}</div><div class="field"><small>license</small>${display(t.license)}</div><div class="field"><small>license_author</small>${display(t.license_author)}</div></div>${t.description ? `<p><small>Description</small><br>${display(t.description)}</p>` : ''}${t.instructions ? `<p><small>Instructions</small><br>${display(t.instructions)}</p>` : ''}${t.cues ? `<p><small>Cues</small><br>${display(t.cues)}</p>` : ''}${t.common_mistakes ? `<p><small>Common mistakes</small><br>${display(t.common_mistakes)}</p>` : ''}${t.search_terms ? `<p><small>Search terms</small><br>${display(t.search_terms)}</p>` : ''}</section>`).join('')}`;
  findExercises();
}

function tableRows(name) {
  const columns = query(`PRAGMA table_info("${name}")`).map(row => row.name);
  const count = scalar(`SELECT COUNT(*) AS value FROM "${name}"`);
  const rows = query(`SELECT * FROM "${name}" LIMIT 300`);
  tableCount.textContent = `${count} row${count === 1 ? '' : 's'}${count > 300 ? ' · showing first 300' : ''}`;
  tableView.innerHTML = `<div class="table-wrap"><table class="data-table"><thead><tr>${columns.map(column => `<th>${escapeHtml(column)}</th>`).join('')}</tr></thead><tbody>${rows.map(row => `<tr>${columns.map(column => `<td>${display(row[column])}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
}

function bindTabs() { document.querySelectorAll('.tab').forEach(tab => tab.addEventListener('click', () => { document.querySelectorAll('.tab,.panel').forEach(item => item.classList.remove('active')); tab.classList.add('active'); document.querySelector(`#${tab.dataset.panel}`).classList.add('active'); })); }
async function start() {
  const SQL = await initSqlJs({ locateFile: file => `https://cdn.jsdelivr.net/npm/sql.js@1.12.0/dist/${file}` });
  const response = await fetch('catalog.db');
  if (!response.ok) throw new Error(`catalog.db could not be loaded (${response.status})`);
  database = new SQL.Database(new Uint8Array(await response.arrayBuffer()));
  renderSummary();
  const tables = query("SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' ORDER BY name").map(row => row.name);
  tableSelect.innerHTML = tables.map(name => `<option value="${escapeHtml(name)}">${escapeHtml(name)}</option>`).join('');
  tableSelect.addEventListener('change', () => tableRows(tableSelect.value));
  tableRows(tableSelect.value);
  search.addEventListener('input', findExercises);
  bindTabs(); findExercises();
  loading.hidden = true; app.hidden = false;
}
start().catch(error => { loading.classList.add('error'); loading.textContent = `Could not load the database: ${error.message}`; });
