class Person {
    var first_name: String
    var last_name: String
    var age: Int

    init(first_name: String, last_name: String, age: Int) {
        self.first_name = first_name   // self expresses you are referring to the properties of the class
        self.last_name = last_name
        self.age = age
    }
    func fullName() -> String {
        return self.first_name + " " + self.last_name
    }
}

enum Subject {
    case Math        // Values defined in an enum (Math to History) are its enumeration cases
    case English
    case French
    case History
}

protocol Classify {                 // Define protocol
    func isStudent() -> Bool
}

class Mentor: Person, Classify {     // List the superclass name before any protocols it adopts
    func isStudent() -> Bool {
        return false
    }

    let subject: Subject

    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
        }

    func stringSubject() -> String {

        switch self.subject {        // Match individual enumeration values with a switch statement
        case Subject.Math:
            return("Math")
        case Subject.English:
            return("English")
        case Subject.French:
            return("French")
        case Subject.History:
            return("History")
            }
        //return String(subject)
        }
}

class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}
