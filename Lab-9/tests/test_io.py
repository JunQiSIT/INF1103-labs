import ast
from pathlib import Path
import pytest

from inventory import Inventory
from oop_inventory_manager import get_positive_float, load_inventory_csv
from supplier import Supplier


def test_get_positive_float_reprompts_on_invalid_input(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    inputs = iter(["abc", "-5", "0", "12.50"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Enter price: ")
    captured = capsys.readouterr().out

    assert result == pytest.approx(12.50)
    assert "Please enter a valid number, e.g. 12.50" in captured
    assert "Please enter a number greater than zero." in captured


def test_load_csv_missing_file_handled_gracefully(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    inv = Inventory.__new__(Inventory)
    inv._products = []
    supplier = Supplier(1, "Default", "default@example.com")
    missing_path = str(tmp_path / "nonexistent_products.csv")

    load_inventory_csv(missing_path, inv, supplier)
    captured = capsys.readouterr().out

    assert "Products file not found" in captured
    assert "Load attempt finished." in captured
    assert len(inv._products) == 0


def test_load_csv_skips_bad_rows_and_loads_valid_rows(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    csv_file = tmp_path / "products.csv"
    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P001,Desk Lamp,25.00,10\n"
        "digital,D001,Photo Editor,49.90,100\n"
        "service,S001,Installation,30.00,5\n"
        "physical,P002,Office Chair,abc,3\n"
        "physical,P003,Monitor Stand,39.50,7\n",
        encoding="utf-8",
    )

    inv = Inventory.__new__(Inventory)
    inv._products = []
    supplier = Supplier(1, "Default", "default@example.com")

    load_inventory_csv(str(csv_file), inv, supplier)
    captured = capsys.readouterr().out

    assert len(inv._products) == 3
    assert "3 products loaded." in captured
    assert "Load attempt finished." in captured
    assert "Skipping invalid row" in captured


def test_no_bare_except_handlers_in_project() -> None:
    project_root = Path(__file__).resolve().parent.parent
    for py_file in project_root.glob("*.py"):
        tree = ast.parse(py_file.read_text(encoding="utf-8"), filename=str(py_file))
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler):
                assert node.type is not None, f"Bare 'except:' found in {py_file.name}:{node.lineno}"
