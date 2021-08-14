/**
 * @param {string} s
 * @return {boolean}
 */
 var isValid = function(s) {
    // create object with closing, opening pairs
    const bracketDict = { ')':'(', '}':'{', ']':'[' };
    // create list of opening parens
    const openParens = Object.values(bracketDict)

    // create empty list of parens seen
    let parensSeen = []
    
    // loop over each char in s
    for (let i = 0; i < s.length; i++ ) {
        let char = s.charAt(i);
        // console.log(char);
        // if char in open paren list, add to parens seen list
        if (openParens.includes(char) ) {
            parensSeen.push(char)
        } 
        // if char not in open parens list
        else {
            console.log(bracketDict.char)
            // if open paren list is empty, return false
            if (openParens.length == 0) {
                return false
            }
            //  if char matches most recent paren in open paren list
            else if (parensSeen[parensSeen.length - 1] == bracketDict[char]) {
                // delete from open paren list and continue
                parensSeen.pop()
            }
            // else return false
            else {
                return false;
            }
        };  

    };

    console.log(parensSeen) 
    return (parensSeen.length == 0)
 }
        


console.log(isValid("()"))
console.log(isValid("{[]}"))
console.log(isValid("([)]"))