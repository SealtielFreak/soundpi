import microdot_asyncio as microdot
from microdot_asyncio import Microdot, Request

app = Microdot()


@app.get('/')
async def index(req: Request):
    return microdot.send_file('templates/index.html')


@app.route("/static/<path:path>")
async def static(request: Request, path):
    if ".." in path:
        return "Not found", 404

    return microdot.send_file("static/" + path)
