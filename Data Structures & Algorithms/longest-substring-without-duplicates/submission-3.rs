impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let s = s.as_bytes(); 
        let mut charz = HashMap::new(); 
        let mut l = 0usize; 
        let mut res = 0; 


        for r in 0..s.len() { 
            if let Some(&idx) = charz.get(&s[r]) {
                l = l.max(idx + 1);
            }
            charz.insert(s[r], r); 
            res = res.max(r-l + 1); 
        }
        return res as i32
    }
}
