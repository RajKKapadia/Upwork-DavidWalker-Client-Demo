import gradio as gr
from fastapi import FastAPI

from client_demo.helper.gradio_ui import demo
from client_demo.routers import home
from client_demo.routers import backend

app = FastAPI()

app = gr.mount_gradio_app(app, demo, path='/gradio')

app.include_router(home.router)
app.include_router(backend.router)
