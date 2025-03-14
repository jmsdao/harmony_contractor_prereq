## What you need
- Have and use a terminal:
  - Have [Docker](https://docs.docker.com/engine/install/) installed (>= version 27.1)
  - Have [Docker Compose](https://docs.docker.com/compose/install/) installed (>=2.29.0)
  - Have [uv](https://docs.astral.sh/uv/getting-started/installation/) installed (>= version 0.5.1)
    - Have Python 3.12 installed with uv: `uv python install 3.12`
- Have [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) installed

## Testing that you pass the prereqs
- Make sure you have the above installed
- `git clone` this repo
- Run `uv sync` to installed the dependencies of this repo
- Run following commands below:
  - `docker compose up --build && docker compose down`
  - `uv run src/foo/python.py`
- Send me a screenshot of the output (there should be no errors)
