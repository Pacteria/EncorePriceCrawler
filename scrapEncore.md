## query string分析

* listing page
  * floor plan B2 listing
    * query string: `myOlePropertyId=640593&MoveInDate=8/1/2022&floorPlans=2322194`
  * floor plan B2B
    * `?myOlePropertyId=640593&MoveInDate=&t=0.07332934253503809&floorPlans=2322196`
  * full listing
    * https://encore.securecafe.com/onlineleasing/encore-at-forest-park/availableunits.aspx?MoveInDate=8/1/2022
    * https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?MoveInDate=8/1/2022
      * rentaloptions这个全一点
      * moveindate只能保证列出所有available unit，实则没有筛选哪些是符合move in date
        * 可能需要自行筛选date available，然后只处理符合我们要求的哪些detail page
* detail page
  * https://encore.securecafe.com/onlineleasing/encore-at-forest-park/rentaloptions.aspx?UnitID=28470723&FloorPlanID=2322194&myOlePropertyid=640593&MoveInDate=8/1/2022
  * ?UnitID=28470723&FloorPlanID=2322194&myOlePropertyid=640593&MoveInDate=8/1/2022
  * move in date是first available两周内
    * 要满足这个条件的才会有pricing
  * slider那里可以选term长度
* props
  * propertyID貌似固定
  * moveindate自选
  * t可以不提供
  * floor plan改一下
    * 2322194: B2
    * 2322196: B2B
  * unitID
    * 房号，这个mapping怎么办？
      * listing里那个onclick的route是hardcoded的

## docker

* 开发完用来打包 
* 开发中还是用venv好一点？