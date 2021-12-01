// Question 1 - Simple Customer Ticketing

// The customer support for an e-commerce business is responsible for answering all open tickets on time. Each open and closed ticket is represented by different open and closed braces respectively, based on the level of complexity to resolve them. For example, the braces “([{“ are open tickets and need a matching braces “}])”, in that order to close these tickets.

// The braces in a string are called balanced if the following conditions are respected:

//     All open braces must be closed and each closed brace must have a matching open brace
//     Any set of nested braces must be closed in order

// Given a 2-dimensional array of strings of braces, verify that the braces in each string are balanced. Return ‘YES’ if all conditions are valid and ‘NO’ otherwise.
// Example

// braces = ['[{}]', '[{]}']

//     The braces in the first string ‘[{}]’ are balanced, because all braces are closed and all nested braces are closed in order.
//     The braces in the second string ‘[{]}’ are not balanced, because the nested brace ‘{‘ was not closed first, so, the order was not respected.
//     The result is [‘YES’, ‘NO’]


// Write your code here. You may add additional functions if you like.
function isMatch(bracesArray) {
  
    const bracesDict = {')':'(', '}':'{', ']':'['};
    
    const openBraces = Object.values(bracesDict);
    
    let bracesSeen = [];
    
    let result = [];
    
    for (let i = 0; i < bracesArray.length; i ++) {
      for (let j = 0; j < bracesArray[i].length; j ++) {
        let char = bracesArray[i].charAt[j];
        
        console.log(char);
        
        if (openBraces.includes(char) ) {
          bracesSeen.push(char);
        }
        else if (bracesSeen[bracesSeen.length -1] == bracesDict[char]) {
          bracesSeen.pop();
        }
        else {
          result.push('NO')
        }
          
      }
      
      
    }
    
    if (bracesSeeen.length == 0) {
        result.push('YES')
      };
    
    console.log(result);
    return result
    
    
    return 'Testing...';
    
  }
  
  isMatch(['[{}]', '[{]}']);
  
  /*
  * Test cases for question 1 - please do not modify
  */
  console.assert(JSON.stringify(isMatch(['[{}]', '[{]}'])) == JSON.stringify(['YES', 'NO']));