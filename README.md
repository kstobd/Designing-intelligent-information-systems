# Проектирование интеллектуальных информационных систем

Этот репозиторий содержит мои лабораторные и практические работы, выполненные в рамках курса "Проектирование интеллектуальных информационных систем".


## Лабораторные работы

### Лабораторная работа 1
- **Файл:** `Выполнение лабы/ПИИС_лаба1.ipynb`
- **Описание:** В этой работе я классифицировал сорт растения ирис по четырем признакам: размерам пестиков и тычинок его цветков. Я обучил модели с разным количеством нейронов и слоев и проанализировал, как это влияет на точность.

### Лабораторная работа 2
- **Файл:** `Выполнение лабы/Lab2.ipynb`
- **Описание:** Я изучал задачу бинарной классификации и построил модель для её решения. Я использовал датасет с двумя классами и обучил модель для их классификации, исследуя влияние различных гиперпараметров на качество модели.

### Лабораторная работа 3
- **Файл:** `Выполнение лабы/Lab3.ipynb`
- **Описание:** Я ознакомился с задачей регрессии, создал и обучил модель для предсказания значений. Я использовал линейную регрессию для предсказания цен на недвижимость на основе различных характеристик домов.

### Лабораторная работа 4
- **Файл:** `Выполнение лабы/Lab4.ipynb`
- **Описание:** Я построил и обучил сверточную нейронную сеть для классификации изображений из набора данных MNIST. В папке также есть файл `draw.py`, который можно запустить и нарисовать свою цифру, которую потом использовать для предсказания.

### Лабораторная работа 5
- **Файл:** `Выполнение лабы/Lab5.ipynb`
- **Описание:** Я построил глубокую сверточную нейронную сеть для классификации изображений из набора CIFAR-10. Я изучил построение модели в Keras в функциональном виде, использовал слой разреживания (Dropout) и обучил модель для классификации изображений по десяти классам.

### Лабораторная работа 6
- **Файл:** `Выполнение лабы/Lab6.ipynb`
- **Описание:** Я прогнозировал успех фильмов по обзорам, построил модель для анализа тональности текста. Я изучил способы представления текста для передачи в ИНС и достиг точности прогноза не менее 95%.

### Лабораторная работа 7
- **Файл:** `Выполнение лабы/Lab7.ipynb`
- **Описание:** Я, как и в прошлой лабораторной работе, написал нейросеть для анализа обзоров, чтобы понять, негативный он или положительный, но в этот раз реализовал рекуррентную нейронную сеть LSTM. Также я сделал ансамбль нейросетей.

### Лабораторная работа 8
- **Файл:** `Выполнение лабы/lab8.ipynb`
- **Описание:** Я сделал рекуррентную нейронную сеть в качестве генеративной модели и обучил её на книге "Алиса в стране чудес". Провел анализ с помощью TensorBoard и ознакомился с callback функциями.

## Практические работы

### Практическая работа 1
- **Файл:** `Выполнение практики/Practice1.ipynb`
- **Описание:** Решение задач, не связанных с машинным обучением, для практики.

### Практическая работа 2
- **Файл:** `Выполнение практики/Practice2.ipynb`
- **Описание:** Я создал модель ИНС, которая способна провести бинарную классификацию по сгенерированным данным.

### Практическая работа 3
- **Файл:** `Выполнение практики/Practice3.ipynb`
- **Описание:** Знакомство с библиотекой NumPy.

### Практическая работа 4
- **Файл:** `Выполнение практики/Practice4.ipynb`
- **Описание:** Я реализовал нейронную сеть, вычисляющую результат заданной логической операции. Затем я реализовал функции, которые будут симулировать работу построенной модели с помощью NumPy.

### Практическая работа 5
- **Файл:** `Выполнение практики/Practice5 вариант 16 цель 3.ipynb`
- **Описание:** Я построил модель, которая содержит в себе автокодировщик и регрессионную модель. Обучил модель и разбил её на три части: модель кодирования данных (Входные данные -> Закодированные данные), модель декодирования данных (Закодированные данные -> Декодированные данные), и регрессионную модель (Входные данные -> Результат регрессии).

### Практическая работа 6
- **Файл:** `Выполнение практики/Practice6.ipynb`
- **Описание:** Я построил сверточную нейронную сеть, которая классифицирует черно-белые изображения с простыми геометрическими фигурами на них.

### Практическая работа 7
- **Файл:** `Выполнение практики/Practice7.ipynb`
- **Описание:** Я построил рекуррентную нейронную сеть, которая прогнозирует значение некоторого периодического сигнала.

### Практическая работа 8
- **Файл:** `Выполнение практики/Practice8.ipynb`
- **Описание:** Я реализовал собственный CallBack и провел обучение модели из практического занятия №6 с написанным CallBack. Построение и сохранение карты признаков на заданных пользователем эпохах. Карта признаков - ядро свертки, представленное в виде изображения. Название карты признака должно иметь вид <номер слоя>_<номер ядра в слое>_<номер эпохи>.
