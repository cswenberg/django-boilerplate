# A Boilerplate for Django Applications
## Installation
Stack
- python3
- virtualenv
- react
- postgres

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Development

Highly encouraged to use [autoenv](https://github.com/kennethreitz/autoenv). Set up environment by:

```bash
cp env.template .env
```

To run django locally:

```bash
python manage.py runserver 0.0.0.0:8000
```
