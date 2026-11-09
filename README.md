# Mahammad Thameez — Portfolio

The portfolio is a FastAPI app that serves the homepage, an About page, individual
project pages, static assets, and a downloadable PDF resume.

## Run locally

From the repository root:

```bash
python3 -m pip install -r requirements.txt
python3 -m uvicorn main:app --reload
```

Open <http://127.0.0.1:8000>.

## Deploy to Render

The repository-root `render.yaml` configures a Python web service. Create a new
Render Blueprint from this repository; Render will install the portfolio
dependencies and start the FastAPI app.

The `Let’s talk` and `Say hello` links open the visitor’s email app with your
email address and a prefilled subject. They do not require a separate mail
service or secret configuration.

The `/resume` route serves `resume.pdf` as a download. Replace that file when
you update your resume.

The `GET /health` endpoint returns `{"status":"ok"}` for uptime checks. The
Render Blueprint configures this route as its service health check.
