Через командную строку SQL:

Для подключения к PostgreSQL: psql -U postgres
Список таблиц в базе данных: \dt
\c "name": для подключения к к базе данных
\list: возвращает список баз данных


CREATE OR REPLACE FUNCTION func1(n text)    ### В скобках хранятся параметры функции с типом данных(int,varchar,text и т.д.)
RETURNS TABLE(result varchar) ### Тип данных которую возвращает функция. Может быть table или простой тип данных(text, int и т.д). Если возвращает table то нужно указаать в скобках переменную и тип данных
AS $$       ### Внутри $$ хранится основной блок функции. В обязательном порядке идет с BEGIN и END.
BEGIN
    IF n = 'phone_number' THEN 
        RETURN QUERY EXECUTE 'SELECT phone_number::varchar FROM phone_book1';       ### После RETURN идет то, что возвращает функция.
    ELSIF n = 'user_name' THEN
        RETURN QUERY EXECUTE 'SELECT user_name FROM phone_book1';
    END IF;     ### После использования условных операторов, обязательно написать end if;
END;
$$ LANGUAGE plpgsql;        ### Указывает, что функция написана на языке PL/pgSQL — это расширенный SQL, позволяющий писать логические конструкции (if, loops и т.д.).

-------------------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE func2(a int, b varchar)
AS $$           ### Как мы видим процедура ничего не возвращает
BEGIN
    if exists( 
        select user_name from phone_book1 where user_name = b       ### exists возвращает True/False. Обычно используется с SELECT чтобы проверить существует ли паттерн в таблице
    ) THEN
        update phone_book1 set phone_number=a where user_name = b;
    else
        insert into phone_book1 (phone_number, user_name) values (a,b);
    end if;
END;
$$ LANGUAGE plpgsql;

---------------------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE func3(
    phone_numbers int[], user_names varchar[], n int            ### Функция или процедура могут принимать в себя списки, в этом случае после типа данных идут квадратные скобки   
)
AS $$
BEGIN
    FOR i IN 1 .. n LOOP
        INSERT INTO phone_book1(phone_number, user_name) VALUES (phone_numbers[i], user_names[i]);
    END LOOP;
END;
$$ LANGUAGE plpgsql;

----------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION func4(a TEXT, b int, c int)
RETURNS TABLE(result varchar) AS $$
BEGIN
    RETURN QUERY EXECUTE format('SELECT %s::varchar FROM phone_book1 LIMIT %s OFFSET %s', a, b, c);     ### После названия столбца может идти ::varchar(или любой другой тип данных), это означает преоброзование значении в столбце на другой тип данных
END;            ### LIMIT означает количество строк которые будут выбраны. OFFSET означает количество строк которые нужно пропустить
$$ LANGUAGE plpgsql;

----------------------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE func5(a varchar)
AS $$
BEGIN
    if exists(
        select phone_number from phone_book1 where phone_number::varchar = a
    ) THEN
        delete from phone_book1 where phone_number::varchar = a; 
    else
        delete from phone_book1 where user_name = a; 
    end if;
END;
$$ LANGUAGE plpgsql;