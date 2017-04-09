function addProject() {
    let form = $("<form>").attr("action", "sayHello()")
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "Project name",
	    "id" : "project-name"
	}))
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "Date",
	    "id" : "project-date"
	}))
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "Techniques",
	    "id" : "techniques"
	}))
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "Github",
	    "id" : "github"
	}))
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "URL small image",
	    "id" : "small-image"
	}))
	.append($("<input>").attr({
	    "type" : "text",
	    "placeholder" : "URL large image",
	    "id" : "large-image"
	}))
	.append($("<textarea>").attr({
	    "type" : "text",
	    "placeholder" : "Short description",
	    "id" : "short-description"
	}))
	.append($("<textarea>").attr({
	    "type" : "text",
	    "placeholder" : "Long description",
	    "id" : "long-description"
	}))
	.append($("<input>")
		.attr({
		    "type" : "submit"
		})
		.val("Submit")
		.click(e => {
		    e.preventDefault()
		    validateForm()
		}))



    $("#table").append(form)
}

function sayHello() {
    console.log("Hello")
}

function validateForm() {
    const name = $("#project-name").val()
    const date = $("#project-date").val()
    const techniques = $("#techniques").val()
    const github = $("#github").val()
    const smallImage = $("#small-image").val()
    const largeImage = $("#large-image").val()
    const shortDescription = $("#short-description").val()
    const longDescription = $("#long-description").val()

    if (name && date && techniques && github &&
	smallImage && largeImage && shortDescription && longDescription) {
	console.log("All is well")
    } else {
	console.log("Noo")
    }
}
