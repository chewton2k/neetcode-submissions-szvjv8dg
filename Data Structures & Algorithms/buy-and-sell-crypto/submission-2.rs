impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = prices[0];
        let mut max_price = 0;

        for &price in &prices { 
            if price < min_price{ 
                min_price = price 
            }
            if price - min_price > max_price{
                max_price = price - min_price
            }
        }

        max_price
    }
}
