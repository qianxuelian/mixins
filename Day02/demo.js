// map
var orders = []
const result = orders.map((order)=>order.amount)
console.log(result)

// function myMap(arr,callback){
//   const result = []
//   for(const item of arr){
//     result.push(callback(item))
//   }
//   return result
// }

// myMap(orders,order=>order.amount)


// filter 告诉程序当前元素是否应该被保留
// 筛选所有已经支付订单
const paidOrders = orders.filter(order=>order.status === 'paid')

function myFilterMap(arr,callback){
  const result = []
  for(const item of arr){
    if(callback(item)){
      result.push(item)
    }
  }
  return result
}

myFilterMap(orders,order=>order.status === 'paid')


// reduce  累加状态
// reduce - 求和
const total = orders.reduce((acc,order)=>{
  if(order.status === 'paid'){
    return acc+order.amount
  }
  return acc
})

function myReduce(arr,callback,initVal){
  const acc = initVal;
  for(const item of arr){
    acc = callback(acc,item)
  }
  return result;
}
myReduce(orders,(sum,order)=>sum+order.amount,0)

// reduce -分组
const groups = orders.reduce((acc,order)=>{
  if(!acc[order.status]){
    acc[order.status] = []
  }
  acc[order.status].push(order.id)
  return acc
},{})



