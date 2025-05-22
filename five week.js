// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler
function isValidPhoneNumber(input) {
  // Remove spaces, hyphens, and parentheses
  const cleaned = input.replace(/[\s\-()]/g, '');

  // Check if cleaned input is 10 digits and numeric
  const isValid = /^\d{10}$/.test(cleaned);

  return isValid;
}

// Sample usage
console.log(isValidPhoneNumber("0987654321"));       // true
console.log(isValidPhoneNumber("(132) 657-776650"));   // false
console.log(isValidPhoneNumber("123-456-5679"));     // true
console.log(isValidPhoneNumber("123"));     // false
console.log(isValidPhoneNumber("12345abc90"));       // false
