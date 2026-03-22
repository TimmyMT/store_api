# 🚀 Run the Server

## Start development server

```bash
uvicorn main:app --reload
```

### Explanation:

* `main` — filename (`main.py`)
* `app` — FastAPI instance inside the file
* `--reload` — auto-reload on code changes (for development only)

---

## Open in browser

* API: http://127.0.0.1:8000
* Swagger docs: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Production (without reload)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## TODO:
```
app/
├── main.py          # entrypoint
├── api/             # роуты (как controllers)
│   └── items.py
├── schemas/         # pydantic модели (DTO)
│   └── item.py
├── services/        # бизнес-логика
│   └── item_service.py
├── models/          # (опционально) ORM модели
│   └── item.py
```

## psql
psql -U postgres
