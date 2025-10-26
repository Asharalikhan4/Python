def update_order():
    chai_type = "Elaichi"
    if True:
        chai_type = "Ashar"
    def kitchen():
        # nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()