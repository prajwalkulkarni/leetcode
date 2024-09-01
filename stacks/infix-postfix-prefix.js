// Infix to prefix/postfix converter: https://raj457036.github.io/Simple-Tools/prefixAndPostfixConvertor.html


//Infix to postfix

const operatorToWeights = {
  '^':3,
  '*':2,
  '/':2,
  '+':1,
  '-':1,
}
function isHigherPrecedence(operator, comparsion){
  let operatorWeight = -1;
  let comparisonWeight = -1;

  const operatorsList = Object.keys(operatorToWeights);
  if(operatorsList.includes(operator)){
    operatorWeight = operatorToWeights[operator]
  }

  if(operatorsList.includes(comparsion)){
    comparisonWeight = operatorToWeights[comparsion];
  }

  return operatorWeight >= comparisonWeight
}

function infixToPostfix(exp){

  const updatedExp = '('+exp+')';
  const stack = [];
  let finalExp = '';
  for(const char of updatedExp){
    if(char === '('){
      stack.push(char);
    }else if(char === ')'){

      while(stack[stack.length - 1] !== '('){
        finalExp += stack.pop();
      }
      stack.pop();
    }else if(Object.keys(operatorToWeights).includes(char)){
      if(isHigherPrecedence(char, stack[stack.length - 1])){
        stack.push(char)
      }else{
        while(!isHigherPrecedence(char, stack[stack.length - 1])){
          finalExp += stack.pop() 
        }
        stack.push(char)
      }
    }else {
      finalExp += char
    }
  }

  return finalExp;
}
