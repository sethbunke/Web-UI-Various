// ADD CODE HERE

// ADD CODE HERE
let forEach = (arr, callback) => {
    //let data = arr;
    for (let i = 0; i < arr.length; i++) {
      arr[i] = callback(arr[i]);
      //output.push(result);
    }
    //arr = output;
  }


// let forEach = (arr, callback) => {
//     for (let i = 0; i < arr.length; i++) {
//       callback(arr[i])
//     }
//   }
  
  let map = (arr, callback) => {
    //let innerArr = arr
    forEach(arr, callback);
    //console.log(innerArr);
    //return innerArr;
    return arr;
  }
  // Uncomment these to check your work!
  console.log(typeof forEach); // should log: 'function'
  //forEach(['a','b','c'], i => console.log(i)); // should log: 'a', 'b', 'c'
  console.log(typeof map); // should log: 'function'
  console.log(map([3,4,5], n => n - 2)); // should log: [1, 2, 3]