from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.calculator import calculate

from app.cidr import calculate_cidr

from app.converter import convert_units


app = FastAPI(
    title="Azure Cloud Utility Platform",
    description="A cloud utility platform built with Azure.",
    version="0.1.0",
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static",
)

templates = Jinja2Templates(directory="app/templates")


class CalculatorRequest(BaseModel):
    operation: str
    a: float
    b: float


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/api/v1/calculator")
def calculator(request: CalculatorRequest):
    try:
        result = calculate(
            request.operation,
            request.a,
            request.b,
        )

        return {
            "operation": request.operation,
            "a": request.a,
            "b": request.b,
            "result": result,
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )

@app.post("/api/v1/cidr")
def cidr_calculate(cidr: str):
    try:
        return calculate_cidr(cidr)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))    


@app.post("/api/v1/convert")
def convert(
    category: str,
    from_unit: str,
    to_unit: str,
    value: float
):
    try:
        result = convert_units(
            category,
            from_unit,
            to_unit,
            value
        )

        return {
            "category": category,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "result": result
        }

    except (ValueError, KeyError) as exc:
        raise HTTPException(status_code=400, detail=str(exc))    