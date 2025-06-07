#0. Arithmetic Operations Function
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            return result
        case "subtract":
            result = num1 - num2
            return result
        case "multiply":
             result = num1 * num2
             return result
        case "divide":
            if num2 == 0:
                result = "Can't be devided"
                return result
            elif num2 > 0 or num2 <0:
                result = num1 / num2
                return result
perform_operation

    