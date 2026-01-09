from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.expense import Expense
from flask_jwt_extended import jwt_required, get_jwt_identity

expense_bp = Blueprint("expenses", __name__, url_prefix="/expenses")


@expense_bp.route("", methods=["POST"])
@jwt_required()
def create_expense():
    data = request.get_json()
    user_id = get_jwt_identity()

    new_expense = Expense(
        description=data["description"],
        amount=data["amount"],
        category=data["category"],
        user_id=user_id
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify(new_expense.to_dict()), 201


@expense_bp.route("", methods=["GET"])
@jwt_required()
def get_expenses():
    user_id = get_jwt_identity()
    expenses = Expense.query.filter_by(user_id=user_id).all()

    return jsonify([expense.to_dict() for expense in expenses]), 200
