function validatePhoneNumber(phone) {
  const phonePattern = /^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$/;
  return phonePattern.test(phone);
}

// Example usage
const phoneNumbers = [
  "123-456-7890",
  "(123) 456-7890",
  "123.456.7890",
  "1234567890",
  "+1 123-456-7890",
  "456-7890",
  "abc-def-ghij"
];

phoneNumbers.forEach((number) => {
  const isValid = validatePhoneNumber(number);
  console.log(`Phone Number: ${number} => Valid: ${isValid}`);
});
