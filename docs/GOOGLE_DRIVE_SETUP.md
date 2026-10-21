# Setting up "Open from Google Drive"

The emulator has an optional **Google Drive** button that lets a player sign in and pick a ROM (or a zip with a ROM) from their own Drive. It stays hidden until you finish the one-time setup below. It takes about 10 minutes and is free.

## What it does and doesn't do

- The browser talks **directly to Google**. No server of yours is involved, and nothing is uploaded.
- It asks only for Google's narrow **"files you pick"** permission (`drive.file`). The emulator can open the one file the player chooses and can't see anything else in their Drive.
- The sign-in lasts only while the page is open. Nothing about the login is stored.
- It only works on a web address (your GitHub Pages site), not on a copy of `index.html` opened from disk. The button simply doesn't appear in that case.
- The Google sign-in and file-picker code is loaded from Google only when a player presses the button. The rest of the emulator still works fully offline.

## One-time setup

You need a Google account and your Pages address, for example `https://juliansoriano.github.io/J-Retro-Emulator/`.

**1. Create a project**
1. Go to https://console.cloud.google.com and sign in.
2. Click the project drop-down at the top, then **New project**. Name it (for example "J Retro Emulator") and create it.

**2. Turn on two Google services**
1. Open **APIs & Services, then Library**.
2. Search for **Google Drive API** and press **Enable**.
3. Search for **Google Picker API** and press **Enable**.

**3. Set up the sign-in screen**
1. Open **APIs & Services, then OAuth consent screen** (it may be called **Google Auth Platform**).
2. Choose **External**, then fill in the app name and your email address.
3. Under **Data access** (or **Scopes**), add the scope `https://www.googleapis.com/auth/drive.file`.
4. While the app is in **Testing** mode, add the Google email addresses of the people allowed to use it as **Test users** (up to 100, including yours).

**4. Create the client ID**
1. Open **Credentials, then Create credentials, then OAuth client ID**.
2. Application type: **Web application**.
3. Under **Authorized JavaScript origins** add `https://juliansoriano.github.io` (just the site, no path and no trailing slash). To try it on your own computer, also add `http://localhost:8000`.
4. Create it and copy the **Client ID** (it ends in `.apps.googleusercontent.com`).

**5. Create the API key**
1. **Create credentials, then API key**, and copy it.
2. Click the key to edit it. Under **Application restrictions** choose **Websites** and add `https://juliansoriano.github.io/*`. Under **API restrictions** choose **Restrict key** and tick **Google Picker API** (and Google Drive API).

**6. Find the project number**
On the project's **Dashboard** (or **Project settings**) copy the **Project number**. It's a long number, not the project name or ID.

**7. Put the three values into the emulator**
Either send them to Claude to add, or edit `src/index.html` yourself. Find this line:

```js
const GOOGLE = { clientId: '', apiKey: '', projectNumber: '' };
```

and fill it in:

```js
const GOOGLE = { clientId: '1234-abc.apps.googleusercontent.com', apiKey: 'AIza...', projectNumber: '123456789012' };
```

Then rebuild and publish:

```
python3 tools/build_single_file.py
git add -A && git commit -m "Add Google Drive settings" && git push
```

These three values are meant to be public in a web page. They are protected by the origin and referrer limits you set in steps 4 and 5, not by being secret. (Never put a "client secret" in the page; this setup doesn't use one.)

## Trying it

Open your Pages site, press **Google Drive**, sign in, and pick a ROM or zip. The game should load and appear in the Library.

## Things players may see

| What they see | Why |
|---|---|
| "Google hasn't verified this app" warning | Normal for apps in Testing mode. They choose **Continue** (only listed test users can). To remove the warning and the 100-user limit, submit the app for Google verification. The narrow `drive.file` permission keeps that review simple. |
| "Access blocked" / "not a test user" | Their email isn't on the Test users list (step 3.4). |
| "Origin mismatch" | The web address isn't listed under Authorized JavaScript origins (step 4.3). |
| Sign-in window doesn't open | The browser blocked the pop-up. Allow pop-ups for the site. |
| Button not visible | The three values are not filled in, or the page was opened from disk rather than from the web address. |
| Picker opens but the file is missing | The picker only shows what the player owns or can access, and only files (not Google Docs). Check the file is in their Drive. |
