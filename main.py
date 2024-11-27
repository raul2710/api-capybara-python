from fastapi import FastAPI
from routes import app_capybara, app_address

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Capybara API",
    description='This API contains a lot of capybaras informations. This project was develope for homework and made for my girl friend that loves and looks capybaras so cute S2',
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar o roteador
app.include_router(app_capybara, prefix="/api", tags=["Capybara"])
app.include_router(app_address, prefix="/api", tags=["Address"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
