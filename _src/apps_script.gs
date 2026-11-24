// ProsBros — приём заявок с prosbros.app: строка в Google-таблицу + письмо на почту.
const SHEET_ID = '1wcNdTTUIQoDxYvBZtaoL_2dpKtey4hKOJQ8wmRPGqLk';
const NOTIFY_TO = 'dauren.makenov@gmail.com';

function doPost(e) {
  const p = (e && e.parameter) || {};
  if (p.website) return out_('ok'); // honeypot: bots fill hidden field
  const clean = function (v) {
    v = String(v || '').trim().slice(0, 300);
    return /^[=+\-@]/.test(v) ? "'" + v : v; // no formulas in the sheet
  };
  const row = [
    Utilities.formatDate(new Date(), 'Asia/Almaty', 'yyyy-MM-dd HH:mm'),
    clean(p.name), clean(p.business), clean(p.email), clean(p.phone),
    clean(p.leads_per_month), p.sms_opt_in === 'true' ? 'да' : 'нет',
    clean(p.site_lang), clean(p.page), clean(p.referrer)
  ];
  const lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    SpreadsheetApp.openById(SHEET_ID).getSheets()[0].appendRow(row);
  } finally {
    lock.releaseLock();
  }
  const labels = ['Время (Алматы)', 'Имя', 'Бизнес', 'Email', 'Телефон', 'Лидов в месяц', 'Согласие на SMS', 'Язык', 'Страница', 'Откуда'];
  const esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]; }); };
  const rows = labels.map(function (l, i) {
    return '<tr><td style="padding:6px 12px 6px 0;color:#6b7280">' + l + '</td><td style="padding:6px 0"><b>' + esc(row[i] || '—') + '</b></td></tr>';
  }).join('');
  const html = '<div style="font-family:Arial,sans-serif;font-size:14px">' +
    '<p style="font-size:16px"><b>Новая заявка на prosbros.app</b></p><table>' + rows + '</table>' +
    '<p><a href="https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/edit">Открыть таблицу заявок</a></p></div>';
  const mail = {
    to: NOTIFY_TO,
    subject: 'ProsBros: новая заявка — ' + (p.name || 'без имени') + (p.business ? ' (' + p.business + ')' : ''),
    htmlBody: html,
    name: 'ProsBros'
  };
  if (/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(p.email || '')) mail.replyTo = p.email;
  MailApp.sendEmail(mail);
  return out_('ok');
}

function doGet() { return out_('ProsBros signup endpoint'); }

function out_(t) { return ContentService.createTextOutput(t); }
