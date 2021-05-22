		normalizationLock = false;
		
		
		replacements = 
			[['11', '2']]
		;

		function createSpreadsheetFormula()
		{
			var extraGoodies = document.getElementById("extraGoodies");

			var spreadsheetFormula = "B2";

			for (var i = 0; i < replacements.length; i++)
			{
				spreadsheetFormula = "SUBSTITUTE(" + spreadsheetFormula + ", \"" + replacements[i][0] + "\", \"" + replacements[i][1] + "\")";
			}

			extraGoodies.innerHTML = "<h3>Equivalent Spreadsheet Formula</h3><p>The worksheet (Excel, LibreOffice) formula for converting text from cell B2 is =" + spreadsheetFormula + "</p>";
		}


		function encodeUnicodeString(aString)
		{
			outputString = "";
			for (var i = 0; i < aString.length; i++)
			{
				var unicodeValueString = aString.codePointAt(i).toString(16);

				while (unicodeValueString.length < 4)
				{
					unicodeValueString = "0" + unicodeValueString;
				}
				outputString += "\\u" + unicodeValueString;
			}

			return outputString;
		}

		function createPythonFormula()
		{
			var pythonFormula = ""

			for (var i = 0; i < replacements.length; i++)
			{
				pythonFormula = pythonFormula + ".replace( \\\"" + encodeUnicodeString(replacements[i][0]) + "\\\", \\\"" + encodeUnicodeString(replacements[i][1]) + "\\\")";
			}

			pythonFormula = "import sys; print(sys.stdin.read()" + pythonFormula + ")";
			var terminalFormula = "python3 -c \"" + pythonFormula + "\"" + " < ./inputFile.txt > ./outputFile.txt"
			extraGoodies.innerHTML = "<h3>Equivalent Terminal Command using Python 3</h3><p>" + terminalFormula + "</p>";

		}

		function viewExcelFormula()
		{
			createSpreadsheetFormula();
		}

		function viewPythonFormula()
		{
			createPythonFormula();
		}

		function setUp()
		{
			setUpLegend();
			// The following call ensures that the
			// checkbox and normalization lock
			// do not become out of sync after a page refresh.
			updateNormalizationLock();
		}

		// Places an explanation of what characters 
		// change when normalization occurs.
		// It places it as a legend the user can read.
		function setUpLegend()
		{
			var legend = document.getElementById("legend");

			var legendMarkup = "<h3>Legend</h3><ul>";

			for (var i = 0; i < replacements.length; i++)
			{
				legendMarkup += "\n<li>" + replacements[i][0] + " becomes " + replacements[i][1] + "</li>";
			}

			legend.innerHTML = legendMarkup;
		}

		function transformCharacters()
		{
			var oldInput = document.getElementById("userInputBox").value;
		
			var newInput = "";
			var replacedCurrentChar = false;
			for (var i = 0; i < oldInput.length; i++)
			{
				replacedCurrentChar = false;
				for (var j = 0; j < replacements.length && !replacedCurrentChar; j++)					
				{
					if (oldInput.substring(i, i + replacements[j][0].length) === replacements[j][0])
					{
						newInput += replacements[j][1];
						i += replacements[j][0].length - 1; // Skip as many characters as we read in., we subtract 1 because the outer for loop will add one for us.
						replacedCurrentChar = true;
					}
				}
				if (!replacedCurrentChar)
				{
					newInput += oldInput.charAt(i);
				}
			}
			document.getElementById("userInputBox").value = newInput;
		
		}

		// Some users may prefer seeing the characters change as they type.
		// This function along with a checkbox allow this behaviour.
		function updateNormalizationLock()
		{
			normalizationLock = document.getElementById("normalizeLock").checked;
		}

		function reactToUserTypingCharacter()
		{
			if (normalizationLock)
			{
				transformCharacters();
			}
		}