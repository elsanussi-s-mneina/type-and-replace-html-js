		
		replacements = 
			[['11', '2']]
		;

		function setUp()
		{
			setUpMoreCharactersPanel();
		}

		function setUpMoreCharactersPanel()
		{
			var panel = document.getElementById("moreCharactersPanel");

			var panelMarkup = "<h2>More Characters</h2>\n<ul>";
			
			var characters = [];

			for (var i = 0; i < replacements.length; i++)
			{
				characters.push(replacements[i][1]);
			}

			// If we had two buttons that put exactly the
			// same text, the user will be confused.
			// Therefore we remove duplicates.
			characters = removeDuplicates(characters);

			for (var i = 0; i < characters.length; i++)
			{
				panelMarkup += "\n<button onclick='typeTextIntoBox(\"" + characters[i] + "\");' style='font-size:x-large; margin: 0.4em; font-family:serif' >" + characters[i] + "</button>";
			}

			panel.innerHTML = panelMarkup;
		}

		function typeTextIntoBox(character)
		{
			// Append the text to the end of the text in the
			// text box.
			// Note: this is not the ideal solution for the situation
			// where the user wants to add a character in the middle
			// of the text.
			document.getElementById("userInputBox").value += character;
		}


		// A function that takes an array
		// and returns a similar array but without
		// any duplicate elements.
		function removeDuplicates(anArray)
		{
			var table = {};
			var anArrayWithoutDuplicates = [];

			for (var i = 0; i < anArray.length; i++)
			{
				table[anArray[i]] = true;
			}

			for (var key in table)
			{
				anArrayWithoutDuplicates.push(key);
			}

			return anArrayWithoutDuplicates;
		}
