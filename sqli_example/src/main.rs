use actix_files as fs;
use actix_web::{get, post, web, App, Error, HttpResponse, HttpServer, Responder};
use tokio;
use tokio_postgres::{NoTls, SimpleQueryMessage};

#[get("/")]
async fn index() -> impl Responder {
    fs::NamedFile::open_async("./static/index.html")
        .await
        .unwrap()
}

#[get("/login")]
async fn login_form() -> impl Responder {
    fs::NamedFile::open_async("./static/login.html")
        .await
        .unwrap()
}


// Safe SQL query construction
#[post("/login")]
async fn handle_login(form: web::Form<LoginCredentials>) -> Result<HttpResponse, Error> {
    let (client, connection) = tokio_postgres::connect(
        "host=localhost user=postgres password=verdad4507 dbname=users_sqli",
        NoTls,
    )
    .await
    .map_err(|e| {
        eprintln!("connection error: {}", e);
        actix_web::error::ErrorInternalServerError("Database connection error")
    })?;

    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });

    let username = &form.username;
    let password = &form.password;

    // Usar una declaración preparada para evitar la inyección SQL
    let stmt = client
        .prepare("SELECT * FROM users WHERE username = $1 AND password = $2")
        .await
        .map_err(|err| {
            eprintln!("Error preparing statement: {}", err);
            actix_web::error::ErrorInternalServerError("Error preparing statement")
        })?;

    // Imprimir la consulta SQL y los parámetros por separado
    println!("Executing SQL: SELECT * FROM users WHERE username = $1 AND password = $2");
    println!("Parameters: username='{}', password='{}'\n", username, password);

    let rows = client
        .query(&stmt, &[username, password])
        .await
        .map_err(|err| {
            eprintln!("Error querying database: {}", err);
            actix_web::error::ErrorInternalServerError("Error querying database")
        })?;

    // Responder con "Invalid credentials" si no hay coincidencias
    if rows.is_empty() {
        Ok(HttpResponse::Unauthorized().body("Invalid credentials"))
    } else {
        Ok(HttpResponse::Ok().body("Login successful"))
    }
}



/* 
// Unsafe SQL query construction
#[post("/login")]
async fn handle_login(form: web::Form<LoginCredentials>) -> Result<HttpResponse, Error> {
    let (client, connection) =
        tokio_postgres::connect("host=localhost user=postgres password=verdad4507 dbname=users_sqli", NoTls).await
            .map_err(|e| {
                eprintln!("connection error: {}", e);
                actix_web::error::ErrorInternalServerError("Database connection error")
            })?;

    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });

    let username = &form.username;
    let password = &form.password;

    // Verificar si el nombre de usuario existe
    let username_sql = format!("SELECT * FROM users WHERE username = '{}'", username);
    println!("Checking username SQL: {}", username_sql);

    let username_messages = client.simple_query(&username_sql).await.map_err(|err| {
        eprintln!("Error querying database: {}", err);
        actix_web::error::ErrorInternalServerError("Error querying database")
    })?;

    let username_rows: Vec<&SimpleQueryMessage> = username_messages.iter().filter(|message| {
        matches!(message, SimpleQueryMessage::Row(_))
    }).collect();

    if username_rows.is_empty() {
        return Ok(HttpResponse::Unauthorized().body("Invalid credentials"));
    }

    // Verificar si el nombre de usuario y la contraseña coinciden
    let password_sql = format!("SELECT * FROM users WHERE username = '{}' AND password = '{}'", username, password);
    println!("Checking password SQL: {}", password_sql);

    let password_messages = client.simple_query(&password_sql).await.map_err(|err| {
        eprintln!("Error querying database: {}", err);
        actix_web::error::ErrorInternalServerError("Error querying database")
    })?;

    let password_rows: Vec<&SimpleQueryMessage> = password_messages.iter().filter(|message| {
        matches!(message, SimpleQueryMessage::Row(_))
    }).collect();

    if password_rows.is_empty() {
        Ok(HttpResponse::Unauthorized().body("Incorrect password"))
    } else {
        Ok(HttpResponse::Ok().body("Login successful"))
    }
}
*/

#[derive(serde::Deserialize)]
struct LoginCredentials {
    username: String,
    password: String,
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let port: u16 = 8080;
    println!("Starting server at http://127.0.0.1:{}", port);

    HttpServer::new(|| {
        App::new()
            .service(index)
            .service(login_form)
            .service(handle_login)
            .service(fs::Files::new("/static", "./static").show_files_listing())
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}
