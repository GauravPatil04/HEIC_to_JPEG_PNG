# 📸 The "No-Nonsense" HEIC Converter

**Finally, a photo converter that respects your privacy and your sanity.😊**

[🌐 Open Website](https://gauravpatil04-heic-to-jpeg-png-app-weys7i.streamlit.app/)


-----

### 😤 The Problem

Let's be real. Converting an iPhone photo to a standard JPEG shouldn't be this hard.
We've all been there: you Google "HEIC to JPG," click the first result, and suddenly:

  * You're bombarded with 50 pop-up ads. 🚫
  * They want you to sign up for a "Premium" trial. 💸
  * **Worst of all:** You have to upload your private memories to some random server, and you have no idea if they keep them.

### 😁 The Solution

I built this tool because I was tired of that.

  * ✅**100% Free forever.** No paywalls.
  * ✅**Zero Ads.** Just a clean tool that does its job.
  * ✅**Privacy First.** This app does not have a database. It doesn't "save" your photos.

### 🧠 How it Works (Transparency Note)

To keep your data safe, this tool processes everything in **RAM (Temporary Memory)**.

1.  You upload a photo.
2.  The script holds it in active memory just long enough to convert it.
3.  You download the result.
4.  **Poof.** 💨 As soon as the session ends or you refresh the page, the data is wiped from the memory. Nothing is ever written to a hard drive storage.

> **⚠️ A Note on Performance:**
> Because we process everything in RAM to protect your privacy, the app does the heavy lifting instantly. If you upload a massive batch (like 100+ high-res photos at once), the server might break a sweat. For the best experience, convert 10-20 photos at a time\!

-----

### ⚙️ Features

  * **Choose Your Format:**
      * **JPEG / JPG:** Best for sharing on WhatsApp, Instagram, or email. (Small size, great quality).
      * **PNG:** Best if you need lossless quality for editing later.
  * **Batch Downloading:** Upload a bunch of photos, and get them back in a single, organized ZIP file.
  * **Smart Naming:** We keep your original filenames so you don't lose track of what is what.

-----

### 💻 For Developers

If you want to run this code yourself or deploy it:

**1. Clone the repo**

```bash
https://github.com/GauravPatil04/HEIC_to_JPEG_PNG.git
```

**2. Install requirements**

```bash
pip install -r requirements.txt
```

**3. Run the app**

```bash
streamlit run app.py
```

-----

*Built with love😊. Enjoy your photos😁\!*