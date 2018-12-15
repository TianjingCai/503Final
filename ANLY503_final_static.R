require(data.table)
require(dplyr)

require(tidyr)
require(dplyr)

library(ggplot2)
library(gridExtra)



alcohol_consump_cap <- fread('total-alcohol-consumption-per-capita-litres-of-pure-alcohol.csv')
attach(alcohol_consump_cap)
setnames(alcohol_consump_cap, c("Entity", "Code", "Year", "Alcohol_consumption_per_capita"))
alcohol_consump_cap_top10 <- alcohol_consump_cap %>% arrange( desc(Alcohol_consumption_per_capita)) %>% top_n(10)





# top 10 country that have highest alcohol consumption capita
ggplot(data = alcohol_consump_cap_top10, aes(x = Entity, y =Alcohol_consumption_per_capita, label = Alcohol_consumption_per_capita)) + labs(x = "Country", y = "Alcohol consumption per capita") +geom_bar(stat = "identity", fill = "purple", width = 0.8) + ggtitle("Total alcohol consumption per capita") +geom_text(aes(label = paste(Alcohol_consumption_per_capita, ' litres')), hjust=-0.1, size=3.5) +coord_flip()

