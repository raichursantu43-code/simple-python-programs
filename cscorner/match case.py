day = "sunday"

match day:
    case "monday":
        print("start of the work week")
    case "friday":
        print("almost weekend")
    case" saterday | sunday":
        print("its weekend")
    case _:
        print("other day")