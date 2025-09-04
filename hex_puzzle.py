def solve_hex_puzzle():
 
    def hex_to_int(hex_str):
        """Convert hex string to integer"""
        return int(hex_str, 16)
    
    def is_valid_prefix(hex_str, k):
        """Check if first k digits satisfy the condition"""
        if k > len(hex_str):
            return False
        prefix = hex_str[:k]
        num = hex_to_int(prefix)
        return num % k == (k - 1)
    
    def is_valid_number(hex_str):
        """Check if entire number satisfies all conditions"""
        n = len(hex_str)
        
        # Check middle digit condition
        middle_idx = n // 2
        if n % 2 == 1:  # odd length
            if hex_str[middle_idx] != '3':
                return False
        else:  # even length - check both middle digits
            if hex_str[middle_idx-1] != '3' and hex_str[middle_idx] != '3':
                return False
        
        # Check prefix conditions
        for k in range(1, n + 1):
            if not is_valid_prefix(hex_str, k):
                return False
        
        return True
    
    def build_number_iteratively():
        """Build the number digit by digit"""
        hex_digits = '0123456789ABCDEF'
        
        # Start with empty string and build up
        current = ""
        max_found = ""
        
        def backtrack(current_str, position):
            nonlocal max_found
            
            if position > 20:  # Reasonable upper limit
                return
            
            # Try each hex digit at current position
            for digit in hex_digits:
                new_str = current_str + digit
                new_len = len(new_str)
                
                # Check if this prefix satisfies the condition
                if is_valid_prefix(new_str, new_len):
                    # Check middle digit constraint for odd lengths
                    middle_ok = True
                    if new_len % 2 == 1:
                        middle_idx = new_len // 2
                        if new_str[middle_idx] != '3':
                            middle_ok = False
                    
                    if middle_ok:
                        # This is a valid number so far
                        if new_len > len(max_found):
                            max_found = new_str
                            print(f"Found valid number of length {new_len}: {new_str}")
                        
                        # Continue building
                        backtrack(new_str, position + 1)
        
        backtrack("", 1)
        return max_found
    
    def verify_solution(hex_str):
        """Verify a solution meets all requirements"""
        print(f"\nVerifying solution: {hex_str}")
        print(f"Length: {len(hex_str)}")
        
        # Check middle digit
        n = len(hex_str)
        middle_idx = n // 2
        if n % 2 == 1:
            print(f"Middle digit (position {middle_idx + 1}): {hex_str[middle_idx]}")
        else:
            print(f"Middle digits: {hex_str[middle_idx-1]}{hex_str[middle_idx]}")
        
        # Check each prefix condition
        print("\nPrefix checks:")
        all_valid = True
        for k in range(1, min(n + 1, 11)):  # Show first 10 for readability
            prefix = hex_str[:k]
            num = hex_to_int(prefix)
            remainder = num % k
            expected = k - 1
            status = "✓" if remainder == expected else "✗"
            print(f"k={k:2d}: {prefix:10s} = {num:8d}, {num} mod {k} = {remainder} (expected {expected}) {status}")
            if remainder != expected:
                all_valid = False
        
        if n > 10:
            print(f"... (showing first 10 of {n} checks)")
        
        return all_valid
    
    print("Solving hex puzzle...")
    print("Looking for longest hex number where each prefix satisfies the divisibility condition")
    print("and the middle digit is 3\n")
    
    # Try the iterative approach
    result = build_number_iteratively()
    
    if result:
        print(f"\nBest solution found: {result}")
        verify_solution(result)
        
        # Convert to decimal for interest
        decimal_val = hex_to_int(result)
        print(f"\nDecimal value: {decimal_val}")
    else:
        print("No solution found!")
    
    return result

# Run the solver
if __name__ == "__main__":
    solution = solve_hex_puzzle()