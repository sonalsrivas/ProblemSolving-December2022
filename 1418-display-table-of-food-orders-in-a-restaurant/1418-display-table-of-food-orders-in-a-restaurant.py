class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dish_list = set()
        table_list = set()
        
        map_table_dishes= defaultdict(dict)
        
        for _, table, dish in orders:
            table=int(table)
            if dish not in map_table_dishes[table]:
                map_table_dishes[table][dish]=1
            else:
                map_table_dishes[table][dish]+=1
            dish_list.add(dish)
            table_list.add(table)
        
        dish_list= sorted(list(dish_list))
        table_list= sorted(list(table_list))
        
        table_columns = ["Table"] + dish_list
        
        result = [table_columns]
        
        for table in table_list:
            result_row = [str(table)]
            for dish in dish_list:
                if dish in map_table_dishes[table]:
                    result_row.append(str(map_table_dishes[table][dish]))
                else:
                    result_row.append("0")
            result.append(result_row)
        return result