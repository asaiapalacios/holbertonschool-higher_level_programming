// Inside func write script: takes an argument and returns true if str is palindrome

func is_palindrome(s: String) -> (Bool) {
     var revs: String = ""

     for character in s.characters {
     	 revs = String(character) + revs // String is reversed & stored in var revs
     }
     return (revs == s)
}
