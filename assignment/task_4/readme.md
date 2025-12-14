# Task 4

## Technical Challanges

### 1. Unstable Connectivity

Farmers often work in place where network is unstable. Offline database must be robust against app termination, low storage condition for the smooth functionality of offline first architecture

### 2. Large Audio Files

Audio files generally are heavy,Users recoding long-duration audio can increase this pain point. Converting the audio to compressed format may reduce the quality for ML processing. Uploading these large files may lead to timeout, user experiencing delay and corrupted transfers etc. Therefore, the system must support resumable uploads, chunked transfer, and exponential backoff for retry attempts.

### 3. Device Limitations and Battery drain

Running offline models require fairly good spec device, which may not be common among farmers. The model must be optimized and quantized to avoid battery drain and executed only when required. The features must be tested against low spec device and should ensure smooth running

### 4. Audio Quality

Since the application heavily depend on mic , hardware damage, issues with mic, improper noise cancellation etc can break the user experience.

### 5. Offline Online Data Consistency

When connectivity returns, multiple pending audio files will be synced. Ensuring correct upload ordering, avoiding duplicate request, maintaining consistent job state  requires idempotent operations, conflict free record identifiers and robust sync logic.


## How I Would Handle Network Latency, Offline Mode & Device Limitations

1. Implement Offline First Architecture with all data writing to the local database and read data from the local to give the user a smooth experience and syncing the data with backend using worker manager. The background worker uploads using exponential backoff and batch uploads.

2. Compress very large files with ML safe compression format. Using streaming or multi part upload and handle partial uploads and retries.

3. Use client generated UUIDs to prevent duplicate job creation

4. Use rule based follow up question generation logic and  light weight custom offline ml model to handle offline situations

5. ML processing of audio will be handled through job queues and will not make the user wait for the ML process to complete.

## Relevant Experience

- 5+ Yr Experience in Full Stack App Development
  - Flutter
  - Django / Python
  - React JS
  - Android
  - Firebase
  - AWS/ Digital Ocean / GCP

- Built audio → STT → transcription pipelines for an AI-assisted scriptwriting tool, including audio processing, transcription, and transcription processing

- Experience with AWS, Firebase, Docker, Celery, Redis, and asynchronous task processing pipelines.

- Built Offline first architecture for multiple apps using databases including sqlite, objectbox and indexed db

- Developed and deployed ML-backed features, such as image classification models integrated into workflows (identify memes from uploaded posts).

- Successfully published and maintained multiple mobile apps and handled full SDLC—from design to deployment.