// Find the first longest word in a text

func longest_word(text: String) -> (String) {
     let problem = text + " " // Var problem never mutated --> change var to let

     var currentWord = ""
     var currentLength = 0

     var max = 0
     var longestWord = ""

     for character in problem.characters {
     	 if character != " " {
	    currentWord += "\(character)"
	    currentLength += 1
	 }
	 else {
	      if currentLength > max {
	      	 max = currentLength
		 longestWord = currentWord // Store longest word in var
	      }
	      currentWord = "" // Repeat process for next word, setting its len to 0
	      currentLength = 0
	 }
     }
     return longestWord							    
}