impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut result:HashMap<[u8; 26], Vec<String>> = HashMap::new(); 

        for s in &strs { 
            let mut count = [0u8; 26];

            for c in s.bytes() { 
                count[(c-b'a') as usize] += 1; 
            }

            result.entry(count).or_default().push(s.clone());
        }
        result.into_values().collect()
    }
}
