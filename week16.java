package org.example.tests;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class SimpleGetTest {

    @Test
    public void testGetRequest() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";

        Response response = RestAssured
                .given()
                .when()
                .get("/posts/1");

        System.out.println("Response Body: " + response.getBody().asString());
        Assert.assertEquals(response.getStatusCode(), 200, "Status code should be 200");
    }
}
