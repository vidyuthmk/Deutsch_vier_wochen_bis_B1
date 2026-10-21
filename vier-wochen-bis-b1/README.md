# Vier Wochen bis B1

A free, static study site for the **telc Deutsch B1** exam: a 28-day plan built around a 9-to-5 job,
420 vocabulary cards, a grammar reference, speaking and writing prompts, exam tactics, ten auto-graded
practice tests (Leseverstehen + Sprachbausteine) and a progress dashboard.

There is no server and no account. **Each visitor's progress is stored in their own browser**
(`localStorage`), so everyone who opens the site sees only their own data. A backup file
(Fortschritt → *Sichern & übertragen*) moves progress to another device.

## Put it online with GitHub Pages

1. Create a new **public** repository on GitHub (for example `vier-wochen-bis-b1`).
2. Upload everything in this folder to the repository root — `index.html`, `fonts/`, `src/`,
   `build.py`, `README.md` and the hidden `.nojekyll` file. (Easiest: *Add file → Upload files*,
   drag the contents of the folder in, commit to `main`.)
3. Open **Settings → Pages**. Under *Build and deployment* choose **Deploy from a branch**,
   branch `main`, folder `/ (root)`, and save.
4. After a minute the site is live at `https://<your-user>.github.io/<repository-name>/`.

Only `index.html` and `fonts/` are needed to run the site; `src/` and `build.py` are for editing.

## Things to know

- **Progress is per browser and per site address.** Clearing the browser's site data, using a private
  window, or switching browser/device starts empty. Download a backup now and then.
- On `<user>.github.io` every project of one account shares a browser origin. Progress is saved under
  the key `vier-wochen-bis-b1:state:v1`, so it will not collide with your other pages.
- Fonts (Archivo, Source Serif 4, IBM Plex Mono — SIL Open Font License, see `fonts/LICENSES.txt`) are
  served from this site; visitors' browsers never contact Google.
- The site loads no third-party scripts, trackers or cookies. The only outside links are the ones in
  the *Prüfung* tab's resource list, which open in a new page when clicked.
- Unofficial material, not affiliated with telc gGmbH. The ten practice tests are original and follow
  the published telc format and point scheme; always also try the official telc Übungstest.

## Editing

```
src/template.html   layout, styles and behaviour
src/data.json       plan, vocabulary, grammar, practice tests
build.py            python3 build.py  →  writes index.html
```

Change content in `src/data.json` (or behaviour in `src/template.html`), run `python3 build.py`, then
commit the new `index.html`. The build checks the data shape before writing.

To preview locally: `python3 -m http.server` in this folder, then open http://localhost:8000.

## Cloud sync later?

GitHub Pages cannot run server code, so true cross-device sync would need an external backend
(for example Firebase or Supabase) plus a login. The state is one small JSON object
(`S` in `src/template.html`, written by `persist()`), so adding sync means reading/writing that object
to the backend inside `persist()` and `loadLocal()`.
