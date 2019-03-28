# YT-transcript-parser


## How to use:

Clone/Download this repo to your folder of choice, and open up your terminal or command prompt and then...

#### 1) Activate virtual environment

From the same folder, run

`. venv/bin/activate`

#### 2) Download necessary dependencies
After navigating to your folder as defined above in your terminal, execute

`pip install -r requirements.txt`

You only need to install these the first time. Don't re-install everytime you run the program.

#### 3) Run the script

`python YT_transcript_parser.py`

**FIRST TIME ONLY**

You'll have to authenticate with your Google Account once, but then you'll be able to just run the file normally afterwards.
- A browser window will open and ask you to allow the **My Transcriber** app access to your YouTube videos. Click yes/allow twice, and you'll end up seeing a message in your browser that verifies authorization. Go back to your terminal/prompt and...

#### 4) Enter the URL of the video

The terminal will ask for a URL of the youtube video you want to parse. Just copy and paste the link and press enter. Your default .doc viewer will then open the parsed file.

## Workflow after the first time

Navigate to the folder as above, and then
  - activate the virtual environment (step 1),
  - run the script (step 3),
  - and enter the URL (step 4).
