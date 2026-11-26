# v4 copy: the Thumbtack partner API only sees leads that arrive after a pro connects,
# so the product works "from now": fast first reply + follow-ups when a customer goes quiet.
# Old leads are not promised anywhere. Built on top of the v3 copy.
import copy
import i18n_v3
from i18n import LANGS
from i18n_extra import EXTRA

V4 = {
 'en': dict(
    feat_h2='From new lead to job on the calendar', f_sms='Text me about my free trial. Msg &amp; data rates may apply. Reply STOP to opt out. Optional.',
    title='ProsBros — Every Thumbtack lead answered in minutes, every quiet one followed up',
    desc="ProsBros answers your new Thumbtack leads in minutes while you're on a job, follows up when customers go quiet, and hands you the ones ready to book — your prices, your words, your OK. For handymen, cleaners, movers and other home-service pros.",
    nav_cta='Try it free', nav_cta_short='Try free',
    h1='Every lead you pay for gets an answer — and a second shot.',
    sub="Bro answers new Thumbtack leads in minutes while you're on a job, follows up when customers go quiet, and hands you the ones ready to book. Your prices. Your words. Your OK.",
    cta1='Get 14 days free', sticky='Get 14 days free', f_btn='Get 14 days free',
    stat3=('12 of 15', 'customers who asked about a real job in our pilot never got an answer.'),
    bridge="So every lead you don't answer fast is money you already spent.",
    pilot_p="An LA handyman paid for every one of his Thumbtack leads and answered what he could between jobs. In our test we texted 493 of his old customers and leads. 19 wrote back, 15 with a real job — and 12 of them never heard back, because he was busy on jobs. The money wasn't lost on bad leads. It was lost on slow answers. That's what Bro fixes: every new lead gets an answer in minutes, and a follow-up if they go quiet.",
    how_h2='How it works',
    how=[('Connect your Thumbtack', "Sign in on Thumbtack's own page — we never see your password. Check the rates Bro will quote. Bro starts with your next lead."),
         ('Every new lead answered in minutes', "Day or night, in your words, at your prices — while you're on a job. Discounts and custom work come to you."),
         ('Quiet customer? Second Shot', 'If a customer stops replying, Bro follows up about their job — after 2 hours, the next day and in 3 days. It stops the second you jump in.'),
         ('Hands you the ones ready to book', 'The second a customer agrees on a price or picks a day, you get a text. You confirm — the job is yours.')],
    feat=[('First Reply: every new lead in minutes', "Day or night, in your words, while you're on a job. Quotes only your rates — never makes up a price."),
          ('Second Shot: quiet customers get a follow-up', 'A short, personal note about their job — not “just checking in.” After 2 hours, the next day and in 3 days. Then it stops.'),
          ("Texts you when it's ready to book", 'Get a text (or WhatsApp / Telegram) the moment a customer agrees on a price or picks a time. You take it from there.'),
          ("Won't make you look bad", 'No double messages. No canned text in the middle of a price talk. Stops the second you jump in. You can see every message.')],
    cmp_row2=('Follows up when a customer goes quiet', 'No', 'If they remember', 'Yes — 3 times, about their job'),
    price_p='At $25–75 a lead, $149 is the price of 2–6 Thumbtack leads. Try it free for 14 days. No contract — cancel anytime. Pay for the year, get 2 months free.',
    plans=[dict(name='Free trial', price='$0', items=['Bro answers your new leads for 14 days', 'See how many customers it saved — in jobs and dollars', 'Cancel before day 14 and pay nothing'], cta='Get 14 days free', kind='free'),
           dict(name='First Reply + Second Shot', price='$149', badge='START HERE', items=['Answers every new lead in minutes, day or night', 'Follow-ups at 2 hrs / next day / 3 days', "Texts you when they're ready to book", 'Quotes only your rates', 'See jobs and dollars it brought in'], cta='Start free trial', kind='top'),
           dict(name='Plus Texts', price='$249', items=['Everything in First Reply + Second Shot', 'Texts customers who said OK — 300 texts/month included', 'Follows up by text when the Thumbtack chat goes quiet', 'Quick quotes from your rate sheet'], cta='Start free trial', kind='plain'),
           dict(name='Crew', price='$499', items=['Everything in Plus Texts', 'More than one account or location', 'One inbox for you and your office person', 'Priority help in US hours'], cta='Talk to us', kind='plain')],
    faq_setup=('How long to get set up?', 'Once your pilot spot opens, about 10 minutes: connect Thumbtack, check your rates, and Bro takes your next lead. Want a hand? Book a free 15-minute call.'),
    faq_old=('What about my old Thumbtack leads?', "Thumbtack's partner connection only shows leads that come in after you connect, so Bro starts with your next one. Past customers whose numbers you have can get a text later — only if they agreed to texts."),
    audit_h2='Stop losing leads you already paid for',
    audit_p="Join the pilot: Bro answers your new Thumbtack leads for 14 days, free. You'll see how many customers it saved — in jobs and dollars. We set up every pro by hand, so spots open in small batches. Leave your info and we'll send your link.",
    audit_list=['No password', 'Nothing goes out without your OK', 'Cancel anytime'],
    chip2='Quiet lead followed up', hl='a second shot',
 ),
 'es': dict(
    feat_h2='Del lead nuevo al jale en tu calendario', f_sms='Mándame textos (SMS) sobre mi prueba gratis. Pueden aplicar cargos por mensajes y datos. Responde STOP para darte de baja. Opcional.',
    title='ProsBros — Cada lead de Thumbtack contestado en minutos y con seguimiento',
    desc='ProsBros contesta tus leads nuevos de Thumbtack en minutos mientras estás en el jale, le da seguimiento a los clientes que dejan de contestar y te pasa los que ya quieren agendar — con tus precios, tus palabras y tu OK. Para handymen, limpieza, mudanzas y todos los pros.',
    nav_cta='Pruébalo gratis', nav_cta_short='Gratis',
    h1='Cada lead que pagas: respuesta rápida y segunda oportunidad.',
    sub='Bro contesta tus leads nuevos de Thumbtack en minutos mientras estás en el jale, le da seguimiento a los clientes que se quedan callados y te pasa los que ya quieren agendar. Tus precios. Tus palabras. Tu OK.',
    cta1='Prueba 14 días gratis', sticky='Prueba 14 días gratis', f_btn='Prueba 14 días gratis',
    stat3=('12 de 15', 'clientes que preguntaron por un jale de verdad en nuestra prueba nunca recibieron respuesta.'),
    bridge='O sea: cada lead que no contestas rápido es lana que ya gastaste.',
    pilot_p='Un handyman de LA pagaba cada lead de Thumbtack y contestaba lo que podía entre jale y jale. En nuestra prueba le textearon a 493 de sus clientes y leads viejos. 19 contestaron, 15 con un jale de verdad — y a 12 de ellos nadie les respondió, porque él andaba trabajando. La lana no se perdió por leads malos. Se perdió por contestar tarde. Eso es lo que arregla Bro: cada lead nuevo recibe respuesta en minutos, y seguimiento si se queda callado.',
    how_h2='Cómo funciona',
    how=[('Conecta tu Thumbtack', 'Entras en la página oficial de Thumbtack — nunca vemos tu password. Checas los precios que va a dar Bro. Bro empieza con tu próximo lead.'),
         ('Cada lead nuevo contestado en minutos', 'De día o de noche, con tus palabras y tus precios, mientras estás en el jale. Descuentos y trabajos especiales te llegan a ti.'),
         ('¿Cliente callado? Second Shot', 'Si un cliente deja de contestar, Bro le da seguimiento sobre su jale — a las 2 horas, al otro día y a los 3 días. Se para en cuanto tú contestas.'),
         ('Te pasa los que ya quieren agendar', 'En cuanto un cliente acepta el precio o escoge día, te llega un texto. Tú confirmas — el jale es tuyo.')],
    feat=[('First Reply: cada lead nuevo en minutos', 'De día o de noche, con tus palabras, mientras estás en el jale. Solo da tus precios — nunca se inventa uno.'),
          ('Second Shot: seguimiento a los que se callan', 'Un mensajito corto y personal sobre su jale — nada de “solo para saber”. A las 2 horas, al otro día y a los 3 días. Y ya.'),
          ('Te textea cuando ya quieren agendar', 'Te llega un texto (o WhatsApp / Telegram) en cuanto un cliente acepta el precio o escoge hora. De ahí sigues tú.'),
          ('No te hace quedar mal', 'Sin mensajes dobles. Nada de textos de plantilla a media negociación. Se para en cuanto tú contestas. Ves cada mensaje.')],
    cmp_row2=('Da seguimiento cuando el cliente se calla', 'No', 'Si se acuerda', 'Sí — 3 veces, sobre su jale'),
    price_p='A $25–75 por lead, $149 es lo que cuestan 2–6 leads de Thumbtack. Pruébalo gratis 14 días. Sin contrato — cancelas cuando quieras. Pagas el año y te regalamos 2 meses.',
    plans=[dict(name='Prueba gratis', price='$0', items=['Bro contesta tus leads nuevos por 14 días', 'Ves cuántos clientes salvó — en jales y en lana', 'Cancelas antes del día 14 y no pagas nada'], cta='Prueba 14 días gratis', kind='free'),
           dict(name='First Reply + Second Shot', price='$149', badge='EMPIEZA AQUÍ', items=['Contesta cada lead nuevo en minutos, de día o de noche', 'Seguimiento a las 2 h / al otro día / a los 3 días', 'Te textea cuando ya quieren agendar', 'Solo da tus precios', 'Ves los jales y la lana que trajo'], cta='Empieza la prueba gratis', kind='top'),
           dict(name='Plus Texts', price='$249', items=['Todo lo de First Reply + Second Shot', 'Textos a clientes que dijeron que sí — 300 textos al mes incluidos', 'Seguimiento por texto cuando la plática en Thumbtack se calla', 'Cotizaciones rápidas con tu lista de precios'], cta='Empieza la prueba gratis', kind='plain'),
           dict(name='Crew', price='$499', items=['Todo lo de Plus Texts', 'Más de una cuenta o ubicación', 'Un solo inbox para ti y tu persona de oficina', 'Ayuda prioritaria en horario de EE. UU.'], cta='Háblanos', kind='plain')],
    faq_setup=('¿Cuánto tardo en configurarlo?', 'Cuando se abra tu lugar en el piloto, unos 10 minutos: conectas Thumbtack, checas tus precios y Bro toma tu próximo lead. ¿Quieres ayuda? Agenda una llamada gratis de 15 minutos.'),
    faq_old=('¿Y mis leads viejos de Thumbtack?', 'La conexión de socios de Thumbtack solo muestra los leads que llegan después de conectar, así que Bro empieza con el próximo. A clientes de antes cuyo número tengas se les puede textear más adelante — solo si aceptaron recibir textos.'),
    audit_h2='Deja de perder leads que ya pagaste',
    audit_p='Únete al piloto: Bro contesta tus leads nuevos de Thumbtack por 14 días, gratis. Vas a ver cuántos clientes salvó — en jales y en lana. Configuramos a cada pro a mano, por eso abrimos lugares en tandas chicas. Déjanos tus datos y te mandamos tu link.',
    audit_list=['Sin password', 'Nada sale sin tu OK', 'Cancelas cuando quieras'],
    chip2='Seguimiento a lead callado', hl='segunda oportunidad',
 ),
 'ru': dict(
    feat_h2='От нового лида до заказа в календаре', f_sms='Пишите мне тексты (SMS) про пробный период. Может взиматься плата за сообщения и данные. Ответь STOP, чтобы отписаться. Необязательно.',
    title='ProsBros — ответ на каждый лид из Thumbtack за минуты и дожим тех, кто замолчал',
    desc='ProsBros отвечает на новые лиды из Thumbtack за минуты, пока ты на объекте, дожимает кастомеров, которые замолчали, и передаёт тебе тех, кто готов записаться — по твоим ценам, твоими словами, с твоего ОК. Для хендименов, клининга, мувинга и других мастеров.',
    nav_cta='Попробовать бесплатно', nav_cta_short='Бесплатно',
    h1='Каждый оплаченный лид — ответ за минуты и второй шанс.',
    sub='Bro отвечает на новые лиды из Thumbtack за минуты, пока ты на объекте, дожимает тех, кто замолчал, и передаёт тебе тех, кто готов записаться. Твои цены. Твои слова. Твоё ОК.',
    cta1='14 дней бесплатно', sticky='14 дней бесплатно', f_btn='Получить 14 дней бесплатно',
    stat3=('12 из 15', 'кастомеров, которые в нашем пилоте спросили про реальный заказ, так и не дождались ответа.'),
    bridge='То есть каждый лид, на который ты не ответил быстро, — это бабки, которые ты уже потратил.',
    pilot_p='Хендимен из LA платил за каждый лид в Thumbtack и отвечал, когда успевал между заказами. В нашем тесте мы написали 493 его старым кастомерам и лидам. 19 ответили, 15 — с реальным заказом, и 12 из них так и не дождались ответа: он был на объектах. Деньги терялись не на плохих лидах, а на медленных ответах. Это Bro и чинит: каждый новый лид получает ответ за минуты, а если замолчал — дожим.',
    how_h2='Как это работает',
    how=[('Подключи Thumbtack', 'Входишь на странице самого Thumbtack — пароль мы не видим. Проверяешь цены, которые будет называть Bro. Bro начинает со следующего лида.'),
         ('Ответ на каждый новый лид за минуты', 'Днём и ночью, твоими словами, по твоим ценам — пока ты на объекте. Скидки и нестандартные работы — к тебе.'),
         ('Кастомер замолчал? Second Shot', 'Если кастомер перестал отвечать, Bro пишет ему про его заказ — через 2 часа, на следующий день и через 3 дня. Отваливает, как только ты подключился.'),
         ('Передаёт тех, кто готов записаться', 'Как только кастомер согласился на цену или выбрал день — тебе приходит текст. Подтверждаешь — заказ твой.')],
    feat=[('First Reply: ответ на каждый лид за минуты', 'Днём и ночью, твоими словами, пока ты на объекте. Называет только твои цены — ничего не выдумывает.'),
          ('Second Shot: дожим тех, кто замолчал', 'Короткое личное сообщение про их заказ — никаких «просто уточняю». Через 2 часа, на следующий день и через 3 дня. И всё.'),
          ('Кидает тебе текст, когда кастомер готов', 'Текст (или WhatsApp / Telegram), как только кастомер согласился на цену или выбрал время. Дальше — ты.'),
          ('Не подставит тебя', 'Без дублей. Без шаблонов посреди торга. Отваливает, как только ты подключился. Каждое сообщение видно тебе.')],
    cmp_row2=('Дожимает, когда кастомер замолчал', 'Нет', 'Если вспомнит', 'Да — 3 раза, про его заказ'),
    price_p='При $25–75 за лид $149 — это цена 2–6 лидов в Thumbtack. Попробуй бесплатно 14 дней. Без контракта — отменить можно в любой момент. Платишь за год — 2 месяца в подарок.',
    plans=[dict(name='Бесплатный пробный период', price='$0', items=['Bro отвечает на твои новые лиды 14 дней', 'Видно, скольких кастомеров он спас — в заказах и долларах', 'Отменишь до 14-го дня — ничего не платишь'], cta='14 дней бесплатно', kind='free'),
           dict(name='First Reply + Second Shot', price='$149', badge='НАЧНИ С ЭТОГО', items=['Отвечает на каждый новый лид за минуты, днём и ночью', 'Дожим через 2 ч / на следующий день / через 3 дня', 'Кидает тебе текст, когда кастомер готов', 'Называет только твои цены', 'Видно заказы и доллары, которые принесло'], cta='Попробовать бесплатно', kind='top'),
           dict(name='Plus Texts', price='$249', items=['Всё из First Reply + Second Shot', 'Тексты кастомерам, которые согласились — 300 SMS в месяц включено', 'Дожим по SMS, когда переписка в Thumbtack заглохла', 'Быстрые эстимейты по твоему прайсу'], cta='Попробовать бесплатно', kind='plain'),
           dict(name='Crew', price='$499', items=['Всё из Plus Texts', 'Несколько аккаунтов или локаций', 'Один инбокс для тебя и диспетчера', 'Приоритетная поддержка в часы США'], cta='Написать нам', kind='plain')],
    faq_setup=('Сколько времени на настройку?', 'Когда откроется твоё место в пилоте — минут 10: подключаешь Thumbtack, проверяешь прайс, и Bro берёт твой следующий лид. Нужна помощь? Запишись на бесплатный звонок на 15 минут.'),
    faq_old=('А мои старые лиды в Thumbtack?', 'Партнёрское подключение Thumbtack показывает только лиды, которые пришли после подключения, поэтому Bro начинает со следующего. Старым кастомерам, чьи номера у тебя есть, можно будет написать по SMS позже — только если они согласились на тексты.'),
    audit_h2='Хватит терять лиды, за которые ты уже заплатил',
    audit_p='Вступай в пилот: Bro 14 дней бесплатно отвечает на твои новые лиды из Thumbtack. Увидишь, скольких кастомеров он спас — в заказах и долларах. Каждого мастера настраиваем вручную, поэтому открываем места небольшими партиями. Оставь контакты — пришлём ссылку.',
    audit_list=['Без пароля', 'Без твоего ОК ничего не уходит', 'Отменить можно в любой момент'],
    chip2='Дожал замолчавшего', hl='второй шанс',
 ),
 'uk': dict(
    feat_h2='Від нового ліда до замовлення в календарі', f_sms='Пишіть мені тексти (SMS) про пробний період. Може стягуватися плата за повідомлення й дані. Відповідай STOP, щоб відписатися. Необов’язково.',
    title='ProsBros — відповідь на кожен лід із Thumbtack за хвилини й дотиск тих, хто замовк',
    desc='ProsBros відповідає на нові ліди з Thumbtack за хвилини, поки ти на об’єкті, дотискає кастомерів, які замовкли, і передає тобі тих, хто готовий записатися — за твоїми цінами, твоїми словами, з твого ОК. Для хендименів, клінінгу, мувінгу та інших майстрів.',
    nav_cta='Спробувати безкоштовно', nav_cta_short='Безкоштовно',
    h1='Кожен оплачений лід — відповідь за хвилини й другий шанс.',
    sub='Bro відповідає на нові ліди з Thumbtack за хвилини, поки ти на об’єкті, дотискає тих, хто замовк, і передає тобі тих, хто готовий записатися. Твої ціни. Твої слова. Твоє ОК.',
    cta1='14 днів безкоштовно', sticky='14 днів безкоштовно', f_btn='Отримати 14 днів безкоштовно',
    stat3=('12 із 15', 'кастомерів, які в нашому пілоті спитали про справжнє замовлення, так і не дочекалися відповіді.'),
    bridge='Тобто кожен лід, на який ти не відповів швидко, — це кеш, який ти вже витратив.',
    pilot_p='Хендимен із LA платив за кожен лід у Thumbtack і відповідав, коли встигав між замовленнями. У нашому тесті ми написали 493 його старим кастомерам і лідам. 19 відповіли, 15 — зі справжнім замовленням, і 12 із них так і не дочекалися відповіді: він був на об’єктах. Гроші губилися не на поганих лідах, а на повільних відповідях. Це Bro і лагодить: кожен новий лід отримує відповідь за хвилини, а якщо замовк — дотиск.',
    how_h2='Як це працює',
    how=[('Підключи Thumbtack', 'Входиш на сторінці самого Thumbtack — пароль ми не бачимо. Перевіряєш ціни, які називатиме Bro. Bro починає з наступного ліда.'),
         ('Відповідь на кожен новий лід за хвилини', 'Удень і вночі, твоїми словами, за твоїми цінами — поки ти на об’єкті. Знижки та нестандартні роботи — до тебе.'),
         ('Кастомер замовк? Second Shot', 'Якщо кастомер перестав відповідати, Bro пише йому про його замовлення — через 2 години, наступного дня й через 3 дні. Відстає, щойно ти підключився.'),
         ('Передає тих, хто готовий записатися', 'Щойно кастомер погодився на ціну чи обрав день — тобі приходить текст. Підтверджуєш — замовлення твоє.')],
    feat=[('First Reply: відповідь на кожен лід за хвилини', 'Удень і вночі, твоїми словами, поки ти на об’єкті. Називає лише твої ціни — нічого не вигадує.'),
          ('Second Shot: дотиск тих, хто замовк', 'Коротке особисте повідомлення про їхнє замовлення — жодних «просто уточнюю». Через 2 години, наступного дня й через 3 дні. І все.'),
          ('Кидає тобі текст, коли кастомер готовий', 'Текст (або WhatsApp / Telegram), щойно кастомер погодився на ціну чи обрав час. Далі — ти.'),
          ('Не підставить тебе', 'Без дублів. Без шаблонів посеред торгу. Відстає, щойно ти підключився. Кожне повідомлення видно тобі.')],
    cmp_row2=('Дотискає, коли кастомер замовк', 'Ні', 'Якщо згадає', 'Так — 3 рази, про його замовлення'),
    price_p='При $25–75 за лід $149 — це ціна 2–6 лідів у Thumbtack. Спробуй безкоштовно 14 днів. Без контракту — скасувати можна будь-коли. Платиш за рік — 2 місяці в подарунок.',
    plans=[dict(name='Безкоштовний пробний період', price='$0', items=['Bro відповідає на твої нові ліди 14 днів', 'Видно, скількох кастомерів він урятував — у замовленнях і доларах', 'Скасуєш до 14-го дня — нічого не платиш'], cta='14 днів безкоштовно', kind='free'),
           dict(name='First Reply + Second Shot', price='$149', badge='ПОЧНИ З ЦЬОГО', items=['Відповідає на кожен новий лід за хвилини, удень і вночі', 'Дотиск через 2 год / наступного дня / через 3 дні', 'Кидає тобі текст, коли кастомер готовий', 'Називає лише твої ціни', 'Видно замовлення й долари, які принесло'], cta='Спробувати безкоштовно', kind='top'),
           dict(name='Plus Texts', price='$249', items=['Усе з First Reply + Second Shot', 'Тексти кастомерам, які погодилися — 300 SMS на місяць включено', 'Дотиск по SMS, коли переписка в Thumbtack заглухла', 'Швидкі естимейти за твоїм прайсом'], cta='Спробувати безкоштовно', kind='plain'),
           dict(name='Crew', price='$499', items=['Усе з Plus Texts', 'Кілька акаунтів або локацій', 'Один інбокс для тебе й диспетчера', 'Пріоритетна підтримка в години США'], cta='Написати нам', kind='plain')],
    faq_setup=('Скільки часу на налаштування?', 'Коли відкриється твоє місце в пілоті — хвилин 10: підключаєш Thumbtack, перевіряєш прайс, і Bro бере твій наступний лід. Потрібна допомога? Запишися на безкоштовний дзвінок на 15 хвилин.'),
    faq_old=('А мої старі ліди в Thumbtack?', 'Партнерське підключення Thumbtack показує лише ліди, що прийшли після підключення, тому Bro починає з наступного. Старим кастомерам, чиї номери в тебе є, можна буде написати по SMS пізніше — лише якщо вони погодилися на тексти.'),
    audit_h2='Годі втрачати ліди, за які ти вже заплатив',
    audit_p='Вступай у пілот: Bro 14 днів безкоштовно відповідає на твої нові ліди з Thumbtack. Побачиш, скількох кастомерів він урятував — у замовленнях і доларах. Кожного майстра налаштовуємо вручну, тому відкриваємо місця невеликими партіями. Залиш контакти — надішлемо посилання.',
    audit_list=['Без пароля', 'Без твого ОК нічого не йде', 'Скасувати можна будь-коли'],
    chip2='Дотиснув того, хто замовк', hl='другий шанс',
 ),
}

SIMPLE = ['title', 'desc', 'nav_cta', 'nav_cta_short', 'h1', 'sub', 'cta1', 'sticky', 'f_btn', 'bridge', 'pilot_p',
          'how_h2', 'how', 'feat', 'price_p', 'plans', 'audit_h2', 'audit_p', 'audit_list', 'feat_h2', 'f_sms']


def apply():
    i18n_v3.apply()  # keeps the v3 pieces that still hold: safety line, compare columns, FAQ additions
    for L in LANGS:
        v = V4[L['code']]
        for k in SIMPLE:
            L[k] = copy.deepcopy(v[k])
        L['stats'] = L['stats'][:2] + [v['stat3']]
        rows = list(L['cmp_rows'])
        rows[1] = v['cmp_row2']
        L['cmp_rows'] = rows
        faq = list(L['faq'])
        faq[3] = v['faq_setup']      # v3 order: price, texts, answer myself, setup, quit, AI, working
        faq.insert(0, v['faq_old'])
        L['faq'] = faq
        X = EXTRA[L['code']]
        X['h1_hl'] = v['hl']
        X['chip2'] = v['chip2']
        assert v['hl'] in L['h1']
