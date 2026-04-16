from cqrs.write_model.session import Session
from cqrs.read_model.session_view import SessionView
from cqrs.projection.session_projection import SessionProjection


def test_projection_flow():
    view = SessionView()
    projection = SessionProjection(view)

    session = Session("s1")

    # старт
    session.start()
    for event in session.events:
        projection.handle(event)

    result = view.get("s1")
    assert result["status"] == "ACTIVE"

    # завершение
    session.finish()
    for event in session.events:
        projection.handle(event)

    result = view.get("s1")
    assert result["status"] == "DONE"