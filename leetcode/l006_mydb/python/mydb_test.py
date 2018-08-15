import unittest
import mydb

class TestMydb(unittest.TestCase):
    def test_set_get_del(self):
        db = mydb.MyDB()
        db.set("a",10)
        self.assertEqual(db.get("a"), 10)
        db.delete("a")
        self.assertEqual(db.get("a"), None)        

    def test_count(self):
        db = mydb.MyDB()
        db.set("a",10)
        db.set("a",20)
        print(db.counter_dict)
        self.assertEqual(db.count(10), 0)
        self.assertEqual(db.count(20), 1)
        
    def test_rollback(self):
        db = mydb.MyDB()
        db.set("a",10)
        db.begin_trans()
        db.set("a", 100)
        db.set("b", 10)                
        self.assertEqual(db.get("a"), 100)
        self.assertEqual(db.get("b"), 10)        
        db.rollback()
        self.assertEqual(db.get("a"), 10)
        self.assertEqual(db.get("b"), None)        
        self.assertEqual(db.rollback(),False)

    def test_nested_rollback(self):
        db = mydb.MyDB()
        db.begin_trans()        
        db.set("a",10)
        self.assertEqual(db.get("a"), 10)
        db.begin_trans()                
        db.set("a", 100)
        db.set("a", 200)        
        self.assertEqual(db.get("a"), 200)
        db.rollback()
        self.assertEqual(db.get("a"), 10)
        db.rollback()
        self.assertEqual(db.get("a"), None)

    def test_commit(self):
        db = mydb.MyDB()
        db.begin_trans()        
        db.set("a",30)
        self.assertEqual(db.get("a"), 30)
        db.begin_trans()                
        db.set("a", 40)
        self.assertEqual(db.get("a"), 40)
        db.commit()
        self.assertEqual(db.get("a"), 40)
        self.assertEqual(db.rollback(), False)

if __name__ == '__main__':
    unittest.main()
