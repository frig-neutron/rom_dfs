#!/usr/bin/env python
import unittest
import romgenseq

class RomGenSeqTest(unittest.TestCase):
  def test_rommat2rels(self): 
    rommat=[
      [0, 2, 0],
      [0, 0, 3],
      [1, 0, 3],
    ]

    rels=romgenseq.objectRel(rommat)

    self.assertEqual(len(rels), 3)
    self.assertEqual(rels[0].oid, 1)
    self.assertEqual(rels[0].rel, [3])
    self.assertEqual(rels[1].oid, 2)
    self.assertEqual(rels[1].rel, [1])
    self.assertEqual(rels[2].oid, 3)
    self.assertEqual(rels[2].rel, [2,3])

  def test_traversal(self):
    def toObjRel(oid, rel=[]): return romgenseq.ObjectRel(oid, rel)

    rels=[
      toObjRel(1, [3]),
      toObjRel(2),
      toObjRel(3, [1,2,4]),
      toObjRel(4, [5]),
      toObjRel(5, [4,8]),
      toObjRel(6),
      toObjRel(7, [6]),
      toObjRel(8, [5,6,7,9]),
      toObjRel(9, [13]),
      toObjRel(10),  
      toObjRel(11),
      toObjRel(12,  [10,11]),
      toObjRel(13,  [9,12])
    ]

    expectedTrav=[2,1,3,11,10,12,13,9,7,6,4,5,8]
    actualTrav=map(
      lambda r: r.oid, 
      romgenseq.objectRelTraverse(rels))

    self.assertEqual(expectedTrav, actualTrav)


if __name__ == '__main__':
  unittest.main()
