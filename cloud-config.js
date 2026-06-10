/* =========================================================================
   Supabase-Zugangsdaten für den optionalen CLOUD-MODUS (gemeinsame Datenbank).

   • Solange url/anonKey leer sind, läuft die App wie bisher rein lokal auf
     dem jeweiligen Gerät (kein Server, offline-fähig).
   • Trägst du hier deine Werte aus Supabase ein, schaltet die App automatisch
     in den Mehrspieler-Modus: alle tippen auf ihren Handys, alles wird live
     synchronisiert.

   Werte findest du in Supabase unter:  Project Settings → API
     - "Project URL"      → url
     - "anon public" key  → anonKey

   ⚠️ NIEMALS den "service_role"-Schlüssel hier eintragen! Nur "anon public".
   ========================================================================= */
window.CLOUD_CONFIG = {
  url: "https://jqtcqsiuglmodxmilccu.supabase.co",
  anonKey: "sb_publishable_-S_yeupTHkrl_XsG2KLb_g_VuaytjOb"
};
