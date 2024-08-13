function fibonacciseries(n){
    const arr = [0,1];

    let startIndex = 1;
    function closure(){
        startIndex+=1;
        if(n<=2){
            return arr.slice(0, n);
        }

        else if(startIndex > n){
            return;
        }

        arr.push(arr[startIndex-1]+arr[startIndex-2])
        closure();
        
    }

    closure();

    return arr;
}
