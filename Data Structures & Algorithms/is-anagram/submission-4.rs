impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len(){ 
            return false;
        }

        let mut counterS: HashMap<u8, i32> = HashMap::new();
        let mut counterT: HashMap<u8, i32> = HashMap::new(); 

        for (a,b) in s.bytes().zip(t.bytes()){
            *counterS.entry(a).or_insert(0) += 1; 
            *counterT.entry(b).or_insert(0) += 1;
        }

        counterS == counterT
    }
}
