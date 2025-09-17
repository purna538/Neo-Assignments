package org.example.tests;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class JsonValidationTest {

    @Test
    public void validateJsonField() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        Response response = RestAssured
                .given()
                .when()
                .get("/posts/1");

        System.out.println("Response Body: " + response.getBody().asString());

        int id = response.jsonPath().getInt("id");
        String title = response.jsonPath().getString("title");

        Assert.assertEquals(id, 1, "ID should be 1");
        Assert.assertFalse(title.isEmpty(), "Title should not be empty");
    }
}
