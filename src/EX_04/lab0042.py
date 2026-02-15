browser_name = input("Enter the browser name\n")
match browser_name:
    case "Firefox":
        print("Execute Firefox code")
      case "Chrome":
        print("Execute Chrome code")
       case "Safari":
        print("Execute Safari code")
       case _:
            print("Browser Not Found")


